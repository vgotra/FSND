import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BaseHttpService } from 'src/app/common/services/BaseHttpService.service';
import { Observable } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';
import { Actor } from './actor.interface';

@Injectable({ providedIn: 'root' })
export class ActorHttpService extends BaseHttpService {
    endpoint: string = '/api/actors';

    constructor(private http: HttpClient) {
        super();
    }

    getById(id: number): Observable<Actor> {
        return this.http.get<Actor>(`${this.endpoint}/${id}`).pipe(retry(1), catchError(this.handleError));
    }
}