import { Injectable } from "@angular/core";
import { BehaviorSubject, Observable } from "rxjs";
import { Entity } from "../interfaces/Entity";

@Injectable({providedIn: 'root'})
export class BaseStoreEntitiesService<T extends Entity> {
    protected _entities: BehaviorSubject<T[]> = new BehaviorSubject(Array<T>());

    public readonly entities$: Observable<T[]> = this._entities.asObservable();

    protected merge(entities: T[]){
        this._entities.next(entities);
    }

    public add(entity: T): void {
        const val = this._entities.getValue();
        val.push(entity);
        this._entities.next(val);
    }

    public getById(id: number): T | undefined {
        return this._entities.getValue().find(x => x.id == id);
    }
}