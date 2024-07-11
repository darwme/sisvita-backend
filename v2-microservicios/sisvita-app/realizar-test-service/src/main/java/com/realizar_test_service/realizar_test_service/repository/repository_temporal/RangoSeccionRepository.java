package com.realizar_test_service.realizar_test_service.repository.repository_temporal;

import com.realizar_test_service.realizar_test_service.model.model_temporal.RangoSeccion;
import com.realizar_test_service.realizar_test_service.service.DataIntegrationService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

@Repository
public class RangoSeccionRepository {

    static private List<RangoSeccion> rangosSeccion= new ArrayList<>();

    // Método para obtener todos los rangos de sección
    public List<RangoSeccion> getAllRangosSeccion() {
        return rangosSeccion;
    }

    // Método para obtener un rango de sección por su ID
    public Optional<RangoSeccion> getRangoSeccionById(Integer idRangoSeccion) {
        return rangosSeccion.stream()
                .filter(rango -> rango.getIdRangoSeccion().equals(idRangoSeccion))
                .findFirst();
    }

    // Método para obtener todos los rangos de sección de una sección específica por su ID
    public List<RangoSeccion> getRangosSeccionBySeccionId(Integer idSeccion) {
        List<RangoSeccion> rangosBySeccionId = new ArrayList<>();
        for (RangoSeccion rango : rangosSeccion) {
            if (rango.getIdSeccion().equals(idSeccion)) {
                rangosBySeccionId.add(rango);
            }
        }
        return rangosBySeccionId;
    }

    // Método para guardar un nuevo rango de sección
    public RangoSeccion saveRangoSeccion(RangoSeccion rangoSeccion) {
        rangosSeccion.add(rangoSeccion);
        return rangoSeccion;
    }

    // Método para actualizar un rango de sección existente
    public RangoSeccion updateRangoSeccion(Integer idRangoSeccion, RangoSeccion rangoSeccion) {
        for (RangoSeccion r : rangosSeccion) {
            if (r.getIdRangoSeccion().equals(idRangoSeccion)) {
                r.setIdSeccion(rangoSeccion.getIdSeccion());
                r.setMinimo(rangoSeccion.getMinimo());
                r.setMaximo(rangoSeccion.getMaximo());
                r.setDiagnostico(rangoSeccion.getDiagnostico());
                return r;
            }
        }
        return null; // Opcional: lanzar excepción si no se encuentra el rango de sección
    }

    // Método para eliminar un rango de sección por su ID
    public void deleteRangoSeccion(Integer idRangoSeccion) {
        rangosSeccion.removeIf(rango -> rango.getIdRangoSeccion().equals(idRangoSeccion));
    }

    public void deleteAllRangoSecciones() {
        rangosSeccion.clear();
    }
}
