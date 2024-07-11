package com.realizar_test_service.realizar_test_service.dto;

import java.util.List;

public class SeccionRequest {

    private int id_seccion;
    private List<Integer> respuestas;

    // Getters y Setters

    public int getId_seccion() {
        return id_seccion;
    }

    public void setId_seccion(int id_seccion) {
        this.id_seccion = id_seccion;
    }

    public List<Integer> getRespuestas() {
        return respuestas;
    }

    public void setRespuestas(List<Integer> respuestas) {
        this.respuestas = respuestas;
    }
}
