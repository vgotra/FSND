import { Injectable } from "@angular/core";
import { Observable } from "rxjs";
import { tap } from "rxjs/operators";
import { BaseStoreEntitiesService } from "../../common/services/BaseStoreEntitiesService.service";
import { Movie } from "../movie/movie.interface";
import { MoviesHttpService } from "./movies.http.service";
import { Movies } from "./movies.interface";

@Injectable({ providedIn: 'root' })
export class MoviesStoreService extends BaseStoreEntitiesService<Movie> {
    constructor(private service: MoviesHttpService) {
        super();
    }

    public LoadEntities(): Observable<Movies> {
        return this.service.getAll().pipe(
            tap((response: Movies) => this.merge(response.movies))
        );
    }
}