package com.realizar_test_service.realizar_test_service.controller;

import com.realizar_test_service.realizar_test_service.model.SeccionRespuesta;
import com.realizar_test_service.realizar_test_service.service.SeccionRespuestaService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/seccion_respuesta/v1")
public class SeccionRespuestaController {

    @Autowired
    private SeccionRespuestaService seccionRespuestaService;

    @GetMapping("/listar")
    public List<SeccionRespuesta> getAllSeccionRespuestas() {
        return seccionRespuestaService.findAll();
    }

    @GetMapping("/{id}")
    public ResponseEntity<SeccionRespuesta> getSeccionRespuestaById(@PathVariable Integer id) {
        return seccionRespuestaService.findById(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @PostMapping
    public SeccionRespuesta createSeccionRespuesta(@RequestBody SeccionRespuesta seccionRespuesta) {
        return seccionRespuestaService.save(seccionRespuesta);
    }
    /*
    @PutMapping("/{id}")
    public ResponseEntity<SeccionRespuesta> updateSeccionRespuesta(@PathVariable Integer id, @RequestBody SeccionRespuesta seccionRespuesta) {
        return ResponseEntity.ok(seccionRespuestaService.update(id, seccionRespuesta));
    }*/

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteSeccionRespuesta(@PathVariable Integer id) {
        seccionRespuestaService.deleteById(id);
        return ResponseEntity.noContent().build();
    }
}