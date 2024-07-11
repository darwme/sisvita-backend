package com.realizar_test_service.realizar_test_service.service;

import com.realizar_test_service.realizar_test_service.model.SeccionRespuesta;
import com.realizar_test_service.realizar_test_service.model.model_temporal.RangoSeccion;
import com.realizar_test_service.realizar_test_service.repository.SeccionRespuestaRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class SeccionRespuestaService {

    @Autowired
    private SeccionRespuestaRepository seccionRespuestaRepository;

    public List<SeccionRespuesta> findAll() {
        return seccionRespuestaRepository.findAll();
    }

    public Optional<SeccionRespuesta> findById(Integer id) {
        return seccionRespuestaRepository.findById(id);
    }

    public SeccionRespuesta save(SeccionRespuesta seccionRespuesta) {
        return seccionRespuestaRepository.save(seccionRespuesta);
    }

    public void deleteById(Integer id) {
        seccionRespuestaRepository.deleteById(id);
    }

}