package com.realizar_test_service.realizar_test_service.model.model_temporal;

import jakarta.persistence.Id;

public class Test {

    private Integer idTest;
    private String nombre;
    private String descripcion;

    // Constructor, getters y setters

    public Test() {
    }

    public Test(Integer idTest, String nombre, String descripcion) {
        this.idTest = idTest;
        this.nombre = nombre;
        this.descripcion = descripcion;
    }

    public Integer getIdTest() {
        return idTest;
    }

    public void setIdTest(Integer idTest) {
        this.idTest = idTest;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getDescripcion() {
        return descripcion;
    }

    public void setDescripcion(String descripcion) {
        this.descripcion = descripcion;
    }
}