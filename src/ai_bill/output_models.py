from typing import Optional
from pydantic import BaseModel, Field

class Paciente(BaseModel):
    """Information about a Patient."""

    # Doc-string for the entity Bill.
    # This doc-string is sent to the LLM as the description of the schema Bill,
    # and it can help to improve extraction results.

    # Note that:
    # 1. Each field is an `optional` -- this allows the model to decline to extract it!
    # 2. Each field has a `description` -- this description is used by the LLM.
    # Having a good description can help improve extraction results.
    name: Optional[str] = Field(default=None, description="Nombre del paciente")
    id: Optional[str] = Field(
        default=None, description="Numero de identificación (ID, CC, TI) del paciente"
    )
    id_type: Optional[str] = Field(
        default=None, description="Tipo de identificacion del paciente, puede ser CC, TI, etc"
    )
    phone_number: Optional[str] = Field(
        default=None, description="Numero de teléfono del paciente"
    )

class Owner(BaseModel):
    """Information about a Client."""

    # Doc-string for the entity Bill.
    # This doc-string is sent to the LLM as the description of the schema Bill,
    # and it can help to improve extraction results.

    # Note that:
    # 1. Each field is an `optional` -- this allows the model to decline to extract it!
    # 2. Each field has a `description` -- this description is used by the LLM.
    # Having a good description can help improve extraction results.
    name: Optional[str] = Field(default=None, description="Nombre del cliente")
    id: Optional[str] = Field(
        default=None, description="Numero de identificacion del cliente"
    )
    id_type: Optional[str] = Field(
        default=None, description="Tipo de identificacion del cliente, puede ser NIT/ID, etc"
    )
    phone_number: Optional[str] = Field(
        default=None, description="Numero de teléfono del cliente"
    )
class Bill(BaseModel):
    """Information about a bill."""

    # Doc-string for the entity Bill.
    # This doc-string is sent to the LLM as the description of the schema Bill,
    # and it can help to improve extraction results.

    # Note that:
    # 1. Each field is an `optional` -- this allows the model to decline to extract it!
    # 2. Each field has a `description` -- this description is used by the LLM.
    # Having a good description can help improve extraction results.
    id: Optional[str] = Field(default=None, description="Codigo de la description del servicio a cobrar")
    description: Optional[str] = Field(
        default=None, description="Descripcion del servicio prestado que se va a facturar"
    )
    quantity: Optional[str] = Field(
        default=None, description="Cantidad de elemntos que se cobran"
    )
    unit_value: Optional[str] = Field(
        default=None, description="Valor total del servicio prestado"
    )
    total_payment: Optional[str] = Field(
        default=None, description="Valor TOTAL A PAGAR de la factura despues de aplicar iva y descuentos"
    )

class Data(BaseModel):
    """Extracted data about people."""

    # Creates a model so that we can extract multiple entities.
    paciente: Paciente
    cliente: Owner
    factura: Bill