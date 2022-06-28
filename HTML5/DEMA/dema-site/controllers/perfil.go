package controllers

import (
	"net/http"
	"time"

	"github.com/gin-gonic/gin"
	"github.com/headyschwi/dema-site/models"
)

func RetornaAluno(c *gin.Context) {
	c.JSON(http.StatusOK, models.Aluno{Nome: "allan", EXP: 0, Nascimento: time.Date(2003, 10, 04, 00, 00, 00, 00, time.Local)})
}
