package com.realizar_test_service.realizar_test_service.service;

import com.realizar_test_service.realizar_test_service.model.model_temporal.*;
import com.realizar_test_service.realizar_test_service.repository.repository_temporal.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

@Service
public class DataIntegrationService {

    private static DataIntegrationService instance;

    private final RestTemplate restTemplate;

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

    // Listas para almacenar los datos cargados
    private List<Usuario> usuarios = new ArrayList<>();
    private List<Test> tests = new ArrayList<>();
    private List<Seccion> secciones = new ArrayList<>();
    private List<RangoSeccion> rangosSeccion = new ArrayList<>();
    private List<RangoTest> rangosTest = new ArrayList<>();

    public List<Usuario> getUsuarios() {
        return new ArrayList<>(usuarios);
    }

    public List<Test> getTests() {
        return new ArrayList<>(tests);
    }

    public List<Seccion> getSecciones() {
        return new ArrayList<>(secciones);
    }

    public List<RangoSeccion> getRangosSeccion() {
        return new ArrayList<>(rangosSeccion);
    }

    public List<RangoTest> getRangosTest() {
        return new ArrayList<>(rangosTest);
    }


    // Constructor privado para Singleton
    private DataIntegrationService(RestTemplate restTemplate) {
        this.restTemplate = restTemplate;
    }

    // Método estático para obtener la instancia Singleton
    public static DataIntegrationService getInstance(RestTemplate restTemplate) {
        if (instance == null) {
            instance = new DataIntegrationService(restTemplate);
        }
        return instance;
    }

    // Método para cargar datos desde todas las APIs externas
    public void cargarDatosDesdeAPIsExternas() {
        cargarUsuariosDesdeAPI();
        cargarTestsDesdeAPI();
        cargarSeccionesDesdeAPI();
        cargarRangosSeccionDesdeAPI();
        cargarRangosTestDesdeAPI();
    }

    // Método para obtener y transformar datos de la API de Usuarios
    private void cargarUsuariosDesdeAPI() {
        ResponseEntity<Usuario[]> response = restTemplate.getForEntity(
                "http://127.0.0.1:5000/usuario/v1/listar", Usuario[].class);

        Usuario[] usuariosArray = response.getBody();
        if (usuariosArray != null) {
            usuarios.addAll(Arrays.asList(usuariosArray));
            for (Usuario usuario : usuariosArray) {
                usuarioRepository.saveUsuario(usuario);
            }
        }
    }

    // Método para obtener y transformar datos de la API de Tests
    private void cargarTestsDesdeAPI() {
        ResponseEntity<Test[]> response = restTemplate.getForEntity(
                "http://127.0.0.1:5000/test/v1/listar", Test[].class);

        Test[] testsArray = response.getBody();
        if (testsArray != null) {
            tests.addAll(Arrays.asList(testsArray));
            for (Test test : testsArray) {
                testRepository.saveTest(test);
            }
        }
    }

    // Método para obtener y transformar datos de la API de Secciones
    private void cargarSeccionesDesdeAPI() {
        ResponseEntity<Seccion[]> response = restTemplate.getForEntity(
                "http://127.0.0.1:5000/seccion/v1/listar", Seccion[].class);

        Seccion[] seccionesArray = response.getBody();
        if (seccionesArray != null) {
            secciones.addAll(Arrays.asList(seccionesArray));
            for (Seccion seccion : seccionesArray) {
                seccionRepository.saveSeccion(seccion);
            }
        }
    }

    // Método para obtener y transformar datos de la API de Rangos de Sección
    private void cargarRangosSeccionDesdeAPI() {
        ResponseEntity<RangoSeccion[]> response = restTemplate.getForEntity(
                "http://127.0.0.1:5000/rango_seccion/v1/listar", RangoSeccion[].class);

        RangoSeccion[] rangosSeccionArray = response.getBody();
        if (rangosSeccionArray != null) {
            rangosSeccion.addAll(Arrays.asList(rangosSeccionArray));
            for (RangoSeccion rangoSeccion : rangosSeccionArray) {
                rangoSeccionRepository.saveRangoSeccion(rangoSeccion);
            }
        }
    }

    // Método para obtener y transformar datos de la API de Rangos de Test
    private void cargarRangosTestDesdeAPI() {
        ResponseEntity<RangoTest[]> response = restTemplate.getForEntity(
                "http://127.0.0.1:5000/rango_test/v1/listar", RangoTest[].class);

        RangoTest[] rangosTestArray = response.getBody();
        if (rangosTestArray != null) {
            rangosTest.addAll(Arrays.asList(rangosTestArray));
            for (RangoTest rangoTest : rangosTestArray) {
                rangoTestRepository.saveRangoTest(rangoTest);
            }
        }
    }

    // Método para limpiar los datos de las listas temporales
    public void limpiarDatos() {
        usuarioRepository.deleteAllUsuarios();
        testRepository.deleteAllTests();
        seccionRepository.deleteAllSecciones();
        rangoSeccionRepository.deleteAllRangoSecciones();
        rangoTestRepository.deleteAllRangoTests();

    }
}
