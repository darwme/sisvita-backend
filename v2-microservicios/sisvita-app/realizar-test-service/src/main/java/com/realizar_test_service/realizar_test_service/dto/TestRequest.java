package com.realizar_test_service.realizar_test_service.dto;

import java.util.List;

public class TestRequest {

    private int id_test;
    private List<SeccionRequest> secciones;

    // Getters y Setters

    public int getId_test() {
        return id_test;
    }

    public void setId_test(int id_test) {
        this.id_test = id_test;
    }

    public List<SeccionRequest> getSecciones() {
        return secciones;
    }

    public void setSecciones(List<SeccionRequest> secciones) {
        this.secciones = secciones;
    }
}
