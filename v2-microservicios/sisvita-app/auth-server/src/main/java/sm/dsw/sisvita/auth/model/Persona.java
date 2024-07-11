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
@Table(name = "persona")
public class Persona {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id_persona;

    @OneToOne
    @JoinColumn(name = "id_usuario", referencedColumnName = "id_usuario")
    private Usuario usuario;

    @Column(name = "nombres")
    private String nombres;

    @Column(name = "apellidos")
    private String apellidos;

    @ManyToOne
    @JoinColumn(name = "ubigeo", referencedColumnName = "ubigeo")
    private Ubicacion ubicacion;

    @Column(name = "fecha_nacimiento")
    private Date fecha_nacimiento;

    @Column(name = "sexo")
    private String sexo;

    @Column(name = "estado_civil")
    private String estado_civil;

    @Column(name = "celular")
    private String celular;

    @Column(name = "tipo_persona")
    private String tipo_persona;

}
