package com.realizar_test_service.realizar_test_service.repository;

import com.realizar_test_service.realizar_test_service.model.SeccionRespuesta;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface SeccionRespuestaRepository extends JpaRepository<SeccionRespuesta, Integer> {
}