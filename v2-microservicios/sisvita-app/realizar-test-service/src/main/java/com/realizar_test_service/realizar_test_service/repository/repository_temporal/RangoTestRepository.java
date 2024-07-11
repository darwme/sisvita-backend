package com.realizar_test_service.realizar_test_service.repository.repository_temporal;

import com.realizar_test_service.realizar_test_service.model.model_temporal.RangoTest;
import com.realizar_test_service.realizar_test_service.service.DataIntegrationService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

@Repository
public class RangoTestRepository {

    static private List<RangoTest> rangosTest= new ArrayList<>();

    // Método para obtener todos los rangos de test
    public List<RangoTest> getAllRangosTest() {
        return rangosTest;
    }

    // Método para obtener un rango de test por su ID
    public Optional<RangoTest> getRangoTestById(Integer idRangoTest) {
        return rangosTest.stream()
                .filter(rango -> rango.getIdRangoTest().equals(idRangoTest))
                .findFirst();
    }

    // Método para obtener todos los rangos de test de un test específico por su ID
    public List<RangoTest> getRangosTestByTestId(Integer idTest) {
        List<RangoTest> rangosByTestId = new ArrayList<>();
        for (RangoTest rango : rangosTest) {
            if (rango.getIdTest().equals(idTest)) {
                rangosByTestId.add(rango);
            }
        }
        return rangosByTestId;
    }

    // Método para guardar un nuevo rango de test
    public RangoTest saveRangoTest(RangoTest rangoTest) {
        rangosTest.add(rangoTest);
        return rangoTest;
    }

    // Método para actualizar un rango de test existente
    public RangoTest updateRangoTest(Integer idRangoTest, RangoTest rangoTest) {
        for (RangoTest r : rangosTest) {
            if (r.getIdRangoTest().equals(idRangoTest)) {
                r.setIdTest(rangoTest.getIdTest());
                r.setMinimo(rangoTest.getMinimo());
                r.setMaximo(rangoTest.getMaximo());
                r.setDiagnostico(rangoTest.getDiagnostico());
                return r;
            }
        }
        return null; // Opcional: lanzar excepción si no se encuentra el rango de test
    }

    // Método para eliminar un rango de test por su ID
    public void deleteRangoTest(Integer idRangoTest) {
        rangosTest.removeIf(rango -> rango.getIdRangoTest().equals(idRangoTest));
    }
    public void deleteAllRangoTests() {
        rangosTest.clear();
    }
}
