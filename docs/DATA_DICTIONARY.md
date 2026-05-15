# Dicionário de Dados — Sleep Health & Daily Performance

Este documento descreve todas as variáveis do dataset `sleep_health_dataset.csv`, incluindo as features originais e as criadas via engenharia de atributos.

## 1. Identificação e Demografia
| Variável | Tipo | Descrição |
| :--- | :--- | :--- |
| **person_id** | Inteiro | Identificador único do indivíduo (removido na modelagem). |
| **age** | Inteiro | Idade do participante. |
| **gender** | Categórico | Gênero (Male, Female, Other). |
| **occupation** | Categórico | Profissão (ex: Software Engineer, Nurse, Doctor). |
| **bmi** | Decimal | Índice de Massa Corporal. |
| **country** | Categórico | País de residência. |

## 2. Arquitetura e Qualidade do Sono
| Variável | Tipo | Descrição |
| :--- | :--- | :--- |
| **sleep_duration_hrs** | Decimal | Total de horas dormidas na última noite. |
| **sleep_quality_score** | Decimal (1-10) | Percepção subjetiva da qualidade do sono. |
| **rem_percentage** | Decimal | Porcentagem do sono na fase REM (regulação emocional). |
| **deep_sleep_percentage** | Decimal | Porcentagem do sono profundo (recuperação física). |
| **sleep_latency_mins** | Inteiro | Tempo em minutos para adormecer. |
| **wake_episodes_per_night**| Inteiro | Número de despertares durante a noite. |
| **sleep_aid_used** | Binário | Uso de medicamentos/auxílios para dormir (0/1). |

## 3. Estilo de Vida e Comportamento
| Variável | Tipo | Descrição |
| :--- | :--- | :--- |
| **caffeine_mg_before_bed** | Inteiro | Miligramas de cafeína antes de dormir. |
| **alcohol_units_before_bed**| Decimal | Unidades de álcool antes de dormir. |
| **screen_time_before_bed_mins**| Inteiro | Uso de telas em minutos antes de deitar. |
| **exercise_day** | Binário | Se praticou exercícios no dia (0/1). |
| **steps_that_day** | Inteiro | Contagem total de passos no dia. |
| **nap_duration_mins** | Inteiro | Duração de cochilos diurnos em minutos. |

## 4. Psicologia e Contexto de Trabalho
| Variável | Tipo | Descrição |
| :--- | :--- | :--- |
| **stress_score** | Decimal (1-10) | Nível de estresse percebido no dia. |
| **work_hours_that_day** | Decimal | Total de horas trabalhadas no dia. |
| **shift_work** | Binário | Trabalho em turnos ou plantão (0/1). |
| **chronotype** | Categórico | Perfil circadiano (Morning, Neutral, Evening). |
| **mental_health_condition** | Categórico | Condição de saúde mental relatada. |

## 5. Ambiente e Saúde Clínica
| Variável | Tipo | Descrição |
| :--- | :--- | :--- |
| **heart_rate_resting_bpm** | Inteiro | Frequência cardíaca em repouso. |
| **room_temperature_celsius**| Decimal | Temperatura do ambiente de sono. |
| **weekend_sleep_diff_hrs** | Decimal | Diferença de sono entre FDS e dias úteis (Social Jetlag). |
| **season** | Categórico | Estação do ano (Summer, Autumn, Winter, Spring). |
| **day_type** | Categórico | Tipo de dia (Weekday, Weekend). |

## 6. Performance e Alvos (Targets)
| Variável | Tipo | Descrição |
| :--- | :--- | :--- |
| **felt_rested** | **Binário** | **Target Primário.** Sentiu-se descansado ao acordar? (0=Não, 1=Sim). |
| **cognitive_performance_score**| Decimal (0-100)| Score de performance mental e foco no dia. |
| **sleep_disorder_risk** | Categórico | Risco de distúrbio (Healthy, Mild, Moderate, Severe). |

## 7. Features Engenheiradas (Advanced Feature Engineering)
| Variável | Fórmula | Objetivo Clínico |
| :--- | :--- | :--- |
| **social_jetlag_factor** | `weekend_sleep_diff_hrs * stress_score` | Mede o impacto do desajuste circadiano sob estresse. |
| **resilience_index** | `sleep_quality_score - stress_score` | Indica a capacidade de manter qualidade de sono sob estresse. |
| **deep_sleep_ratio** | `deep_sleep_percentage / (rem_percentage + deep_sleep_percentage)` | Proporção relativa de recuperação física no ciclo. |
| **sleep_efficiency** | `(rem_percentage + deep_sleep_percentage) / 100` | Percentual do sono em fases restauradoras. |
| **stress_work_interaction** | `stress_score * work_hours_that_day` | Mede a carga cumulativa de fadiga ocupacional. |

> Nota: essas 5 features correspondem ao script otimizado atual `05_neural_network_optimized.py`. O notebook principal ainda pode conter células exploratórias anteriores com subconjunto diferente de features; para a V1 oficial, considerar o script como referência de execução.
