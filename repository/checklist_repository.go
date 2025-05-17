package repository

import (
	"builder-list/models"

	"gorm.io/gorm"
)

type ChecklistRepository struct {
  db *gorm.DB
}

func NewChecklistRepository(db *gorm.DB) *ChecklistRepository{
  return &ChecklistRepository{db}
}

func (pkg *ChecklistRepository) FindById(id int) (interface{} , error){
  checklist := models.Checklist{}
  pkg.db.First(&checklist.ID, id)
  return checklist, nil
}

func (pkg *ChecklistRepository) FindAll() (interface{} , error){
  checklist := []models.Checklist{}
  pkg.db.Find(&checklist)
  return checklist, nil
}

func (pkg *ChecklistRepository) Delete(id int) error {
  pkg.db.Delete(&models.Checklist{}, id)
  return nil
}

func (pkg *ChecklistRepository) Create(checklist *models.Checklist) error {
  pkg.db.Create(checklist)
  return nil
}


