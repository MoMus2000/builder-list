package models

import (
	"gorm.io/gorm"
)

type Checklist struct {
	gorm.Model
  ID        uint `gorm:"primaryKey"`
  Name      string
  ProjectID uint
}

