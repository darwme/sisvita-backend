package sm.dsw.sisvita.auth.model;

import jakarta.persistence.*;
import lombok.*;


@Entity
@Getter
@Setter
@Builder
@AllArgsConstructor
@NoArgsConstructor
@Table(name = "especialista")
public class Especialista {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id_especialista;

    @OneToOne
    @JoinColumn(name = "id_persona", referencedColumnName = "id_persona")
    private Persona persona;

    @Column(name = "codigo_especialista", unique = true)
    private String codigo_especialista;

    @Column(name = "especialidad")
    private String especialidad;

    @Column(name = "experiencia")
    private String experiencia;

}

