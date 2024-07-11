package sm.dsw.sisvita.auth.model;

import jakarta.persistence.*;
import lombok.*;
import java.util.Date;

@Entity
@Getter
@Setter
@Builder
@AllArgsConstructor
@NoArgsConstructor
@Table(name = "paciente")
public class Paciente {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id_paciente;

    @OneToOne
    @JoinColumn(name = "id_persona", referencedColumnName = "id_persona")
    private Persona persona;

    @Column(name = "codigo_paciente", unique = true)
    private String codigo_paciente;

    @Column(name = "antecedentes")
    private String antecedentes;
}
