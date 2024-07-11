package com.realizar_test_service.realizar_test_service.model.model_temporal;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;


public class RangoTest {

    private Integer idRangoTest;
    private Integer idTest; // Referencia al Test
    private Integer minimo;
    private Integer maximo;
    private String diagnostico;

    // Constructor, getters y setters

    public RangoTest() {
    }

    public RangoTest(Integer idRangoTest, Integer idTest, Integer minimo, Integer maximo, String diagnostico) {
        this.idRangoTest = idRangoTest;
        this.idTest = idTest;
        this.minimo = minimo;
        this.maximo = maximo;
        this.diagnostico = diagnostico;
    }

    public Integer getIdRangoTest() {
        return idRangoTest;
    }

    public void setIdRangoTest(Integer idRangoTest) {
        this.idRangoTest = idRangoTest;
    }

    public Integer getIdTest() {
        return idTest;
    }

    public void setIdTest(Integer idTest) {
        this.idTest = idTest;
    }

    public Integer getMinimo() {
        return minimo;
    }

    public void setMinimo(Integer minimo) {
        this.minimo = minimo;
    }

    public Integer getMaximo() {
        return maximo;
    }

    public void setMaximo(Integer maximo) {
        this.maximo = maximo;
    }

    public String getDiagnostico() {
        return diagnostico;
    }

    public void setDiagnostico(String diagnostico) {
        this.diagnostico = diagnostico;
    }
}