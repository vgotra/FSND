import { Injectable } from "@angular/core";
import { Observable } from "rxjs";
import { tap } from "rxjs/operators";
import { BaseStoreEntitiesService } from "../../common/services/BaseStoreEntitiesService.service";
import { ActorsHttpService } from "./actors.http.service";
import { Actor } from "./actors.interface";

@Injectable({ providedIn: 'root' })
export class ActorsStoreService extends BaseStoreEntitiesService<Actor> {
    constructor(private service: ActorsHttpService) {
        super();
    }

    public LoadEntities(): Observable<Actor[]> {
        return this.service.getAll().pipe(
            tap((response: Actor[]) => this.merge(response))
        );
    }
}