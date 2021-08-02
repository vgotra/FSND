import { Injectable } from "@angular/core";
import { Observable } from "rxjs";
import { tap } from "rxjs/operators";
import { BaseStoreEntityService } from "src/app/common/services/BaseStoreEntityService.service";
import { ActorHttpService } from "./actor.http.service";
import { Actor } from "./actor.interface";

@Injectable({ providedIn: 'root' })
export class ActorStoreService extends BaseStoreEntityService<Actor> {
    constructor(private service: ActorHttpService) {
        super();
    }

    public LoadEntity(id: number): Observable<Actor> {
        return this.service.getById(id).pipe(
            tap((response: Actor) => this.set(response))
        );
    }
}