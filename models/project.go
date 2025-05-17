package models

import "gorm.io/gorm"

type Project struct{
  gorm.Model
  ID uint `gorm:"primaryKey"`
  Name string `gorm:"not null"`
  Description string
  Checklist Checklist `gorm:"foreignKey:ProjectID;constraint:OnUpdate:CASCADE,OnDelete:SET NULL;"`
}

