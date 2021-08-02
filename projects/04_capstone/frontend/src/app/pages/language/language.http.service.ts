import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BaseHttpService } from 'src/app/common/services/BaseHttpService.service';
import { Observable } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';
import { Language } from './language.interface';

@Injectable({ providedIn: 'root' })
export class LanguageHttpService extends BaseHttpService {
    endpoint: string = 'languages';

    constructor(private http: HttpClient) {
        super();
    }

    getById(id: number): Observable<Language> {
        return this.http.get<Language>(`${this.endpoint}/${id}`).pipe(retry(1), catchError(this.handleError));
    }
}