from fastapi import APIRouter, HTTPException, Depends, status

router = APIRouter(prefix="/auth", tags=["auth"])