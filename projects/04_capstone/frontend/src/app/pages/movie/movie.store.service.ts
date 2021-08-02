import { Injectable } from "@angular/core";
import { Observable } from "rxjs";
import { tap } from "rxjs/operators";
import { BaseStoreEntityService } from "src/app/common/services/BaseStoreEntityService.service";
import { MovieHttpService } from "./movie.http.service";
import { Movie } from "./movie.interface";

@Injectable({ providedIn: 'root' })
export class MovieStoreService extends BaseStoreEntityService<Movie> {
    constructor(private service: MovieHttpService) {
        super();
    }

    public LoadEntity(id: number): Observable<Movie> {
        return this.service.getById(id).pipe(
            tap((response: Movie) => this.set(response))
        );
    }
}