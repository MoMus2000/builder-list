package models

import (
	"gorm.io/gorm"
)

type Checklist struct {
	gorm.Model
  ID uint
  ProjectID uint
  Project Project `gorm:"foreignKey:ProjectID;constraint:OnUpdate:CASCADE,OnDelete:SET NULL;"`
}

