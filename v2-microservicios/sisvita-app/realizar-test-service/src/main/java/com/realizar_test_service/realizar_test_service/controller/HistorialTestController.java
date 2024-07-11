package com.realizar_test_service.realizar_test_service.controller;

import com.realizar_test_service.realizar_test_service.model.HistorialTest;
import com.realizar_test_service.realizar_test_service.service.HistorialTestService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/historial_test/v1")
public class HistorialTestController {

    @Autowired
    private HistorialTestService historialTestService;

    @GetMapping("/listar")
    public List<HistorialTest> getAllHistorialTests() {
        return historialTestService.findAll();
    }

    @GetMapping("/{id}")
    public ResponseEntity<HistorialTest> getHistorialTestById(@PathVariable Integer id) {
        return historialTestService.findById(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @PostMapping
    public HistorialTest createHistorialTest(@RequestBody HistorialTest historialTest) {
        return historialTestService.save(historialTest);
    }

    @PutMapping("/{id}")
    public ResponseEntity<HistorialTest> updateHistorialTest(@PathVariable Integer id, @RequestBody HistorialTest historialTest) {
        return ResponseEntity.ok(historialTestService.update(id, historialTest));
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteHistorialTest(@PathVariable Integer id) {
        historialTestService.deleteById(id);
        return ResponseEntity.noContent().build();
    }
}