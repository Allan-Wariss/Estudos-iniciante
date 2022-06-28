package routes

import (
	"github.com/gin-gonic/gin"
	"github.com/headyschwi/dema-site/controllers"
)

func HandleRequests() {
	r := gin.Default()
	r.GET("/perfil", controllers.RetornaAluno)
	r.Run(":8000")
}
