package com.realizar_test_service.realizar_test_service.service;


import com.realizar_test_service.realizar_test_service.dto.SeccionRequest;
import com.realizar_test_service.realizar_test_service.model.SeccionRespuesta;
import com.realizar_test_service.realizar_test_service.model.HistorialTest;
import com.realizar_test_service.realizar_test_service.model.model_temporal.*;
import com.realizar_test_service.realizar_test_service.repository.*;
import com.realizar_test_service.realizar_test_service.repository.repository_temporal.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import java.util.List;
import java.util.ArrayList;
import java.util.Date;
import java.time.LocalDateTime;

@Service
public class RealizarTestService {

    @Autowired
    private DataIntegrationService dataIntegrationService;

    @Autowired
    private UsuarioRepository usuarioRepository;

    @Autowired
    private TestRepository testRepository;

    @Autowired
    private SeccionRepository seccionRepository;

    @Autowired
    private RangoSeccionRepository rangoSeccionRepository;

    @Autowired
    private RangoTestRepository rangoTestRepository;

    @Autowired
    private HistorialTestRepository historialTestRepository;

    @Transactional
    public void realizarTest(int idUsuario, int idTest, List<SeccionRequest> secciones) {

        // Cargar datos necesarios desde las APIs externas
        dataIntegrationService.cargarDatosDesdeAPIsExternas();

        // Crear instancia de Usuario y Test
        Usuario usuario = usuarioRepository.getUsuarioById(idUsuario)
                .orElseThrow(() -> new RuntimeException("Usuario no encontrado"));

        Test test = testRepository.getTestById(idTest)
                .orElseThrow(() -> new RuntimeException("Test no encontrado"));

        // Listas para almacenar puntajes y diagnósticos
        List<Integer> puntajes = new ArrayList<>();
        List<String> diagnosticos = new ArrayList<>();

        // Procesar cada sección
        for (SeccionRequest seccionRequest : secciones) {
            Seccion seccion = seccionRepository.getSeccionById(seccionRequest.getId_seccion())
                    .orElseThrow(() -> new RuntimeException("Sección no encontrada"));

            // Transformar respuestas a String separado por comas
            String respuestasStr = String.join(",", seccionRequest.getRespuestas().stream()
                    .map(String::valueOf)
                    .toArray(String[]::new));

            // Crear instancia de SeccionRespuesta
            SeccionRespuesta seccionRespuesta = new SeccionRespuesta(usuario.getIdUsuario(),test.getIdTest(),seccion.getIdSeccion(),respuestasStr);

            // Guardar la SeccionRespuesta en la base de datos
            seccionRepository.saveSeccion(seccion);

            // Calcular puntaje de la sección y diagnosticar
            int puntajeSeccion = calcularPuntaje(seccionRequest.getRespuestas());
            puntajes.add(puntajeSeccion);

            String diagnosticoSeccion = calcularDiagnostico(puntajeSeccion, seccion);
            if (diagnosticoSeccion != null) {
                diagnosticos.add(diagnosticoSeccion);
            }
        }

        // Calcular puntaje total y diagnóstico del test
        int puntajeTotal = puntajes.stream().mapToInt(Integer::intValue).sum();
        String diagnosticoTest = calcularDiagnosticoTotal(puntajeTotal, test);

        LocalDateTime fechaActual = LocalDateTime.now();
        String estado="no evaluado";
        // Crear instancia de HistorialTest
        HistorialTest historialTest = new HistorialTest(
                usuario.getIdUsuario(),
                test.getIdTest(),
                fechaActual,
                String.join(",", puntajes.toString()),
                String.join(",", diagnosticos.toString()),
                estado

        );

        // Guardar HistorialTest en la base de datos
        historialTestRepository.save(historialTest);

        // Limpiar datos temporales
        dataIntegrationService.limpiarDatos();
    }

    private int calcularPuntaje(List<Integer> respuestas) {
        return respuestas.stream().mapToInt(Integer::intValue).sum();
    }

    private String calcularDiagnostico(int puntaje, Seccion seccion) {
        List<RangoSeccion> rangos = rangoSeccionRepository.getAllRangosSeccion();
        for (RangoSeccion rango : rangos) {
            if (rango.getMinimo() <= puntaje && puntaje <= rango.getMaximo()) {
                return rango.getDiagnostico();
            }
        }
        return null;
    }

    private String calcularDiagnosticoTotal(int puntajeTotal, Test test) {
        List<RangoTest> rangos = rangoTestRepository.getAllRangosTest();
        for (RangoTest rango : rangos) {
            if (rango.getMinimo() <= puntajeTotal && puntajeTotal <= rango.getMaximo()) {
                return rango.getDiagnostico();
            }
        }
        return null;
    }

}
