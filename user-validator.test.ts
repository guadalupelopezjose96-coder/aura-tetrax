import { UserValidator } from '../src/domain/UserValidator';

describe('UserValidator - FourPhonix Standards', () => {
  
  // Test de Casos Positivos
  test('Debería retornar TRUE para correos válidos al 100%', () => {
    const validEmails = ['admin@fourphonix.com', 'user.test@domain.io', 'dev@sub.fourphonix.com'];
    validEmails.forEach(email => {
      expect(UserValidator.isValidEmail(email)).toBe(true);
    });
  });

  // Test de Casos Negativos
  test('Debería retornar FALSE para formatos de correo inválidos', () => {
    const invalidEmails = ['correo-sin-arroba.com', '@sinusuario.com', 'espacios @domain.com', ''];
    invalidEmails.forEach(email => {
      expect(UserValidator.isValidEmail(email)).toBe(false);
    });
  });

  // Test de Seguridad (Anti-ReDoS)
  test('Debería manejar strings extremadamente largos sin colapsar el sistema', () => {
    const maliciousEmail = "a".repeat(10000) + "@domain.com";
    const start = Date.now();
    UserValidator.isValidEmail(maliciousEmail);
    const duration = Date.now() - start;
    
    expect(duration).toBeLessThan(50); // El test falla si tarda más de 50ms
  });
});
