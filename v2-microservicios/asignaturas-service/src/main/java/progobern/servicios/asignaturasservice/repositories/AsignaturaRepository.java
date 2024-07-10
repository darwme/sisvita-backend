package progobern.servicios.asignaturasservice.repositories;

import progobern.servicios.asignaturasservice.models.Asignatura;
import org.springframework.data.mongodb.repository.MongoRepository;
import progobern.servicios.asignaturasservice.models.Profesor;
import progobern.servicios.asignaturasservice.models.Tesis;

import java.util.List;
import java.util.UUID;

public interface AsignaturaRepository extends MongoRepository<Asignatura, UUID> {
    public List<Asignatura> findByTesis(Tesis tesis);
    public List<Asignatura> findByProfesor(Profesor profesor);
    public Asignatura findByCodigoAndSeccion(Integer codigo,Integer seccion);
}
