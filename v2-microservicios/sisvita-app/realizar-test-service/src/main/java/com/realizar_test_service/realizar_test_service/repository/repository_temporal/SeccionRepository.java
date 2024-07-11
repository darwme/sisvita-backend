package com.realizar_test_service.realizar_test_service.repository.repository_temporal;

import com.realizar_test_service.realizar_test_service.model.model_temporal.Seccion;
import com.realizar_test_service.realizar_test_service.service.DataIntegrationService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

@Repository
public class SeccionRepository {

    static private List<Seccion> secciones= new ArrayList<>();


    // Método para obtener todas las secciones
    public List<Seccion> getAllSecciones() {
        return secciones;
    }

    // Método para obtener una sección por su ID
    public Optional<Seccion> getSeccionById(Integer idSeccion) {
        return secciones.stream()
                .filter(seccion -> seccion.getIdSeccion().equals(idSeccion))
                .findFirst();
    }

    // Método para obtener todas las secciones de un test específico por su ID
    public List<Seccion> getSeccionesByTestId(Integer idTest) {
        List<Seccion> seccionesByTestId = new ArrayList<>();
        for (Seccion seccion : secciones) {
            if (seccion.getIdTest().equals(idTest)) {
                seccionesByTestId.add(seccion);
            }
        }
        return seccionesByTestId;
    }

    // Método para guardar una nueva sección
    public Seccion saveSeccion(Seccion seccion) {
        secciones.add(seccion);
        return seccion;
    }

    // Método para actualizar una sección existente
    public Seccion updateSeccion(Integer idSeccion, Seccion seccion) {
        for (Seccion s : secciones) {
            if (s.getIdSeccion().equals(idSeccion)) {
                s.setIdTest(seccion.getIdTest());
                s.setDescripcion(seccion.getDescripcion());
                return s;
            }
        }
        return null; // Opcional: lanzar excepción si no se encuentra la sección
    }

    // Método para eliminar una sección por su ID
    public void deleteSeccion(Integer idSeccion) {
        secciones.removeIf(seccion -> seccion.getIdSeccion().equals(idSeccion));
    }
    public void deleteAllSecciones() {
        secciones.clear();
    }
}
