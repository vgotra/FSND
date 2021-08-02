import { Injectable } from "@angular/core";
import { BehaviorSubject, Observable } from "rxjs";
import { Entity } from "../interfaces/Entity";

@Injectable({providedIn: 'root'})
export class BaseStoreEntityService<T extends Entity> {
    protected _entity: BehaviorSubject<T> = new BehaviorSubject(Object.create({}));

    public readonly entity$: Observable<T> = this._entity.asObservable();

    public get(): T | undefined {
        return this._entity.getValue();
    }

    public set(entiry: T): void {
        this._entity.next(entiry);
    }
}