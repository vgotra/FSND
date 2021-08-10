import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BaseHttpService } from 'src/app/common/services/BaseHttpService.service';
import { Observable } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';
import { Movie } from './movie.interface';

@Injectable({ providedIn: 'root' })
export class MovieHttpService extends BaseHttpService {
    endpoint: string = '/api/movies';

    constructor(private http: HttpClient) {
        super();
    }

    getById(id: number): Observable<Movie> {
        return this.http.get<Movie>(`${this.endpoint}/${id}`).pipe(retry(1), catchError(this.handleError));
    }
}