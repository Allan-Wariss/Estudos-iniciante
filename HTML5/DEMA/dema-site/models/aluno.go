package models

import (
	"time"

	"gorm.io/gorm"
)

type Aluno struct {
	gorm.Model
	Nome               string    `json:"nome"`
	EXP                int       `json:"exp"`
	Nascimento         time.Time `json:"nascimento"`
	Cursos_Finalizados []Curso   `json:"cursos_finalizados"`
}

var aluno []Aluno
