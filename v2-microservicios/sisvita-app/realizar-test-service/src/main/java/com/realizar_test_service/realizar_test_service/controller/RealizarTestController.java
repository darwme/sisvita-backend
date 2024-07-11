package com.realizar_test_service.realizar_test_service.controller;

import com.realizar_test_service.realizar_test_service.dto.TestRequest;
import com.realizar_test_service.realizar_test_service.service.RealizarTestService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/gestor_realizar_test/v1")
public class RealizarTestController {

    private final RealizarTestService realizarTestService;

    @Autowired
    public RealizarTestController(RealizarTestService realizarTestService) {
        this.realizarTestService = realizarTestService;
    }

    @PostMapping("/realizar_test/{idUsuario}")
    public ResponseEntity<?> realizarTest(
            @PathVariable int idUsuario,
            @RequestBody TestRequest testRequest
    ) {
        try {

            realizarTestService.realizarTest(idUsuario, testRequest.getId_test(), testRequest.getSecciones());
            return ResponseEntity.status(HttpStatus.CREATED).body("Test realizado correctamente.");
        } catch (Exception e) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body("Error al realizar el test: " + e.getMessage());
        }
    }
}
