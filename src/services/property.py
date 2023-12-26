from sqlalchemy.orm import Session

from models.property import Property
from dto import property


def create_property(data: property.Property, db: Session):
    property = Property(
        points=data.points,
        health=data.health,
        energy=data.energy,
        ammunition=data.ammunition,
        user_id=data.user_id
    )

    try:
        db.add(property)
        db.commit()
        db.refresh(property)
    except Exception as e:
        print(e)
    
    return property

def get_property(db: Session, property_id: int):
    return db.query(Property).filter(Property.id==property_id).first()

def update_property(data: property.Property, db: Session, property_id: int):
    property = db.query(Property).filter(Property.id==property_id).first()
    property.points = data.points
    property.health = data.health
    property.energy = data.energy
    property.ammunition = data.ammunition

    db.add(property)
    db.commit()
    db.refresh(property)

    return property

def delete_property(db: Session, property_id: int):
    property = db.query(Property).filter(Property.id==property_id).delete()
    db.commit()

    return property
