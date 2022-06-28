package models

import "gorm.io/gorm"

type Curso struct {
	gorm.Model
	Nome               string  `json:"nome"`
	Dificuldade        string  `json:"dificuldade"`
	EXP                int     `json:"exp"`
	Cursos_Necessarios []Curso `json:"curso_necessarios"`
}
