import React, { useState } from 'react';
import { TextField, Button, Paper, Typography, Box } from '@mui/material';
import { Equation } from '../types';

interface EquationFormProps {
  onSubmit: (a: number, b: number, c: number) => void;
  initialValues?: Omit<Equation, 'id' | 'result'>;
  isEditing?: boolean;
}

const EquationForm: React.FC<EquationFormProps> = ({ 
  onSubmit, 
  initialValues = { a: 0, b: 0, c: 0 },
  isEditing = false
}) => {
  const [a, setA] = useState<number>(initialValues.a);
  const [b, setB] = useState<number>(initialValues.b);
  const [c, setC] = useState<number>(initialValues.c);
  const [errors, setErrors] = useState<{ a?: string; b?: string; c?: string }>({});

  const validate = (): boolean => {
    const newErrors: { a?: string; b?: string; c?: string } = {};
    let isValid = true;

    if (a === null || isNaN(Number(a))) {
      newErrors.a = 'Hệ số a phải là số';
      isValid = false;
    }

    if (b === null || isNaN(Number(b))) {
      newErrors.b = 'Hệ số b phải là số';
      isValid = false;
    }

    if (c === null || isNaN(Number(c))) {
      newErrors.c = 'Hệ số c phải là số';
      isValid = false;
    }

    setErrors(newErrors);
    return isValid;
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (validate()) {
      onSubmit(Number(a), Number(b), Number(c));
    }
  };

  return (
    <Paper elevation={3} sx={{ p: 3, mb: 3 }}>
      <Typography variant="h5" gutterBottom>
        {isEditing ? 'Sửa phương trình' : 'Nhập phương trình bậc 2'}
      </Typography>
      <Typography variant="subtitle1" gutterBottom>
        ax² + bx + c = 0
      </Typography>
      <Box component="form" onSubmit={handleSubmit}>
        <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 2, alignItems: 'flex-start', mb: 2 }}>
          <Box sx={{ minWidth: 120, flex: '1 1 auto' }}>
            <TextField
              label="Hệ số a"
              type="number"
              fullWidth
              value={a}
              onChange={(e) => setA(Number(e.target.value))}
              error={!!errors.a}
              helperText={errors.a}
              required
            />
          </Box>
          <Box sx={{ minWidth: 120, flex: '1 1 auto' }}>
            <TextField
              label="Hệ số b"
              type="number"
              fullWidth
              value={b}
              onChange={(e) => setB(Number(e.target.value))}
              error={!!errors.b}
              helperText={errors.b}
              required
            />
          </Box>
          <Box sx={{ minWidth: 120, flex: '1 1 auto' }}>
            <TextField
              label="Hệ số c"
              type="number"
              fullWidth
              value={c}
              onChange={(e) => setC(Number(e.target.value))}
              error={!!errors.c}
              helperText={errors.c}
              required
            />
          </Box>
          <Box sx={{ display: 'flex', gap: 2, alignItems: 'center' }}>
            <Button 
              type="submit" 
              variant="contained" 
              color="primary"
            >
              {isEditing ? 'Cập nhật' : 'Tính toán'}
            </Button>
            {!isEditing && (
              <Button 
                type="button" 
                variant="contained" 
                color="success"
                onClick={handleSubmit}
              >
                Thêm
              </Button>
            )}
          </Box>
        </Box>
      </Box>
    </Paper>
  );
};

export default EquationForm;