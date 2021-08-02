import { Injectable } from "@angular/core";
import { Observable } from "rxjs";
import { tap } from "rxjs/operators";
import { BaseStoreEntitiesService } from "../../common/services/BaseStoreEntitiesService.service";
import { GenresHttpService } from "./genres.http.service";
import { Genre } from "./genres.interface";

@Injectable({ providedIn: 'root' })
export class GenresStoreService extends BaseStoreEntitiesService<Genre> {
    constructor(private service: GenresHttpService) {
        super();
    }

    public LoadEntities(): Observable<Genre[]> {
        return this.service.getAll().pipe(
            tap((response: Genre[]) => this.merge(response))
        );
    }
}