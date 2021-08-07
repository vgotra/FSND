import { Injectable } from "@angular/core";
import { Observable } from "rxjs";
import { tap } from "rxjs/operators";
import { BaseStoreEntitiesService } from "../../common/services/BaseStoreEntitiesService.service";
import { Genre } from "../genre/genre.interface";
import { Genres } from "./genres.interface";
import { GenresHttpService } from "./genres.http.service";

@Injectable({ providedIn: 'root' })
export class GenresStoreService extends BaseStoreEntitiesService<Genre> {
    constructor(private service: GenresHttpService) {
        super();
    }

    public LoadEntities(): Observable<Genres> {
        return this.service.getAll().pipe(
            tap((response: Genres) => this.merge(response.genres))
        );
    }
}