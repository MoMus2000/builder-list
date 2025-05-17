package repository

type Repository interface{
  Delete(id int) error
  Create(interface{}) error
  FindById(id int) (interface{}, error)
  FindAll() (interface{}, error)
}

