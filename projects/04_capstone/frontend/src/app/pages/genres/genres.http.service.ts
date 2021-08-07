import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BaseHttpService } from 'src/app/common/services/BaseHttpService.service';
import { Observable } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';
import { Genres } from './genres.interface';

@Injectable({ providedIn: 'root' })
export class GenresHttpService extends BaseHttpService {
    endpoint: string = 'genres';

    constructor(private http: HttpClient) {
        super();
    }

    getAll(): Observable<Genres> {
        return this.http.get<Genres>(this.endpoint).pipe(retry(1), catchError(this.handleError));
    }
}