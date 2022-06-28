package database

import (
	"gorm.io/driver/postgres"
	"gorm.io/gorm"
)

var (
	DB  *gorm.DB
	err error
)

func DatabaseConnect() {
	connectionString := ""
	DB, err = gorm.Open(postgres.Open(connectionString))
}
