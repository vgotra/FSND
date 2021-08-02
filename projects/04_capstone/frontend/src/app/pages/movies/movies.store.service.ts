import { Injectable } from "@angular/core";
import { Observable } from "rxjs";
import { tap } from "rxjs/operators";
import { BaseStoreEntitiesService } from "../../common/services/BaseStoreEntitiesService.service";
import { MoviesHttpService } from "./movies.http.service";
import { Movie } from "./movies.interface";

@Injectable({ providedIn: 'root' })
export class MoviesStoreService extends BaseStoreEntitiesService<Movie> {
    constructor(private service: MoviesHttpService) {
        super();
    }

    public LoadEntities(): Observable<Movie[]> {
        return this.service.getAll().pipe(
            tap((response: Movie[]) => this.merge(response))
        );
    }
}