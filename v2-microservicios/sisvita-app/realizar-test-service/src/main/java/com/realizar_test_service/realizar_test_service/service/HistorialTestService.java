package com.realizar_test_service.realizar_test_service.service;

import com.realizar_test_service.realizar_test_service.model.HistorialTest;
import com.realizar_test_service.realizar_test_service.repository.HistorialTestRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class HistorialTestService {

    @Autowired
    private HistorialTestRepository historialTestRepository;

    public List<HistorialTest> findAll() {
        return historialTestRepository.findAll();
    }

    public Optional<HistorialTest> findById(Integer id) {
        return historialTestRepository.findById(id);
    }

    public HistorialTest save(HistorialTest historialTest) {
        return historialTestRepository.save(historialTest);
    }

    public void deleteById(Integer id) {
        historialTestRepository.deleteById(id);
    }

    public HistorialTest update(Integer id, HistorialTest historialTest) {
        return historialTestRepository.findById(id)
                .map(existingTest -> {
                    existingTest.setIdUsuario(historialTest.getIdUsuario());
                    existingTest.setIdTest(historialTest.getIdTest());
                    existingTest.setPuntajes(historialTest.getPuntajes());
                    existingTest.setDiagnosticos(historialTest.getDiagnosticos());
                    existingTest.setEstado(historialTest.getEstado());
                    return historialTestRepository.save(existingTest);
                })
                .orElseThrow(() -> new RuntimeException("Test not found with id " + id));
    }
}