package routes

import (
	"github.com/gofiber/fiber/v2"
)

type ChecklistRouter struct {}

func NewCheckListRoute() ChecklistRouter {
  return ChecklistRouter{}
}

func (cl *ChecklistRouter) ViewCheckList(c *fiber.Ctx) error {
  return c.Render(
    "checklist", nil,
  )
}

