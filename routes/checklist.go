package routes

import (
	"builder-list/repository"

	"github.com/gofiber/fiber/v2"
)

type ChecklistRouter struct {
  cr *repository.ChecklistRepository
}

func NewCheckListRoute(cr *repository.ChecklistRepository) ChecklistRouter {
  return ChecklistRouter{cr}
}

func (cl *ChecklistRouter) ViewCheckList(c *fiber.Ctx) error {
  // projectId, _ := strconv.Atoi(c.Params("checklist"))

  return c.Render(
    "checklist", fiber.Map{
      "ProjectName": "",
    },
  )
}

func (cl *ChecklistRouter) ListAllCheckList(c *fiber.Ctx) error {
  // projectId, _ := strconv.Atoi(c.Params("checklist"))

  checklists, _ := cl.cr.FindAll()

  return c.JSON(
    fiber.Map{
      "checklist": checklists,
      },
    )
}


