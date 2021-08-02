import { Injectable } from "@angular/core";
import { Observable } from "rxjs";
import { tap } from "rxjs/operators";
import { BaseStoreEntityService } from "src/app/common/services/BaseStoreEntityService.service";
import { GenreHttpService } from "./genre.http.service";
import { Genre } from "./genre.interface";

@Injectable({ providedIn: 'root' })
export class GenreStoreService extends BaseStoreEntityService<Genre> {
    constructor(private service: GenreHttpService) {
        super();
    }

    public LoadEntity(id: number): Observable<Genre> {
        return this.service.getById(id).pipe(
            tap((response: Genre) => this.set(response))
        );
    }
}