import { Injectable } from "@angular/core";
import { Observable } from "rxjs";
import { tap } from "rxjs/operators";
import { BaseStoreEntitiesService } from "../../common/services/BaseStoreEntitiesService.service";
import { Actor } from "../actor/actor.interface";
import { ActorsHttpService } from "./actors.http.service";
import { Actors } from "./actors.interface";

@Injectable({ providedIn: 'root' })
export class ActorsStoreService extends BaseStoreEntitiesService<Actor> {
    constructor(private service: ActorsHttpService) {
        super();
    }

    public LoadEntities(): Observable<Actors> {
        return this.service.getAll().pipe(
            tap((response: Actors) => this.merge(response.actors))
        );
    }
}