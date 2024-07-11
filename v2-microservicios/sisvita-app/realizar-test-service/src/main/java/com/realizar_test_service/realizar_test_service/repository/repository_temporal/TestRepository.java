package com.realizar_test_service.realizar_test_service.repository.repository_temporal;

import com.realizar_test_service.realizar_test_service.model.model_temporal.Test;
import com.realizar_test_service.realizar_test_service.service.DataIntegrationService;
import org.springframework.stereotype.Repository;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

@Repository
public class TestRepository {

    static private List<Test> tests= new ArrayList<>();

    // Método para obtener todos los tests
    public List<Test> getAllTests() {
        return tests;
    }

    // Método para obtener un test por su ID
    public Optional<Test> getTestById(Integer idTest) {
        return tests.stream()
                .filter(test -> test.getIdTest().equals(idTest))
                .findFirst();
    }

    // Método para guardar un nuevo test
    public Test saveTest(Test test) {
        tests.add(test);
        return test;
    }

    // Método para actualizar un test existente
    public Test updateTest(Integer idTest, Test test) {
        for (Test t : tests) {
            if (t.getIdTest().equals(idTest)) {
                t.setNombre(test.getNombre());
                t.setDescripcion(test.getDescripcion());
                return t;
            }
        }
        return null; // Opcional: lanzar excepción si no se encuentra el test
    }

    // Método para eliminar un test por su ID
    public void deleteTest(Integer idTest) {
        tests.removeIf(test -> test.getIdTest().equals(idTest));
    }
    public void deleteAllTests() {
        tests.clear();
    }
}
