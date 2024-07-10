package sisvita.servicios.authservice.repositories;

import sisvita.servicios.authservice.models.Asignatura;
import org.springframework.data.mongodb.repository.MongoRepository;
import sisvita.servicios.authservice.models.Profesor;
import sisvita.servicios.authservice.models.Tesis;

import java.util.List;
import java.util.UUID;

public interface AsignaturaRepository extends MongoRepository<Asignatura, UUID> {
    public List<Asignatura> findByTesis(Tesis tesis);
    public List<Asignatura> findByProfesor(Profesor profesor);
    public Asignatura findByCodigoAndSeccion(Integer codigo,Integer seccion);
}
