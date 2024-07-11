package com.realizar_test_service.realizar_test_service.model.model_temporal;

import jakarta.persistence.Id;

public class Seccion {

    private Integer idSeccion;
    //private Integer idTest; // Referencia al Test
    private String descripcion;

    // Constructor, getters y setters

    public Seccion() {
    }

    public Seccion(Integer idSeccion, String descripcion) {
        this.idSeccion = idSeccion;
        //this.idTest = idTest;
        this.descripcion = descripcion;
    }

    public Integer getIdSeccion() {
        return idSeccion;
    }

    public void setIdSeccion(Integer idSeccion) {
        this.idSeccion = idSeccion;
    }
    /*
    public Integer getIdTest() {
        return idTest;
    }

    public void setIdTest(Integer idTest) {
        this.idTest = idTest;
    }*/

    public String getDescripcion() {
        return descripcion;
    }

    public void setDescripcion(String descripcion) {
        this.descripcion = descripcion;
    }
}